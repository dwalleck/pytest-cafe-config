# -*- coding: utf-8 -*-

import inspect
import os

from cafe.configurator.managers import TestEnvManager
from cafe.common.reporting import cclogging
import pytest
from cafe.drivers.unittest.runner import UnittestRunner


def pytest_addoption(parser):
    group = parser.getgroup('cafe-config')
    group.addoption(
        '--cafe-proj',
        action='store',
        dest='cafe_proj',
        help='Name of the project to test'
    )

    group.addoption(
        '--cafe-config',
        action='store',
        dest='cafe_config',
        help='Name of the Cafe configuration file for the project to use'
    )


def pytest_configure(config):
    
    if config.getoption('cafe_proj') and config.getoption('cafe_config'):
        # Setting test repo path variables to pass checks
        # to validate if the test repos exist
        os.environ['CAFE_ALLOW_MANAGED_ENV_VAR_OVERRIDES'] = '1'
        os.environ['CAFE_TEST_REPO_PATH'] = config.args[0]
        test_env = TestEnvManager(
            config.getoption('cafe_proj'),
            config.getoption('cafe_config') + '.config',
            test_repo_package_name=config.args[0])
        test_env.finalize()
        cclogging.init_root_log_handler()
        UnittestRunner.print_mug_and_paths(test_env)


def pytest_collection_modifyitems(items, config):
    selected_items = []
    deselected_items = []

    for item in items:
        if item.parent and 'fixture' not in item.parent.name.lower():
            selected_items.append(item)
        else:
            deselected_items.append(item)
    config.hook.pytest_deselected(items=deselected_items)
    items[:] = selected_items


@pytest.fixture
def bar(request):
    return request.config.option.cafe_proj
