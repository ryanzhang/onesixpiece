# -*- coding: UTF-8 -*-

import sys
import pytest
import logging  # pragma: no cover

# 初始化日志
logging.basicConfig(
    level=logging.INFO, format=" %(asctime)s - %(levelname)s- %(message)s"
)

# each test runs on cwd to its temp dir
@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    logging.info("\n=======================request start=================================")
    logging.info("request.module=" + str(request.module))
    logging.info("request.function=" + str(request.function))
    logging.info("request.cls=" + str(request.cls))
    logging.info("request.fspath=" + str(request.fspath))
    logging.info("request.fixturenames=" +  str(request.fixturenames))
    logging.info("request.fixturename=" +  str(request.fixturename))
    logging.info("request.scope" +  str(request.scope))
    logging.info("\n=======================request end=================================")
    # Get the fixture dynamically by its name.
    tmpdir = request.getfixturevalue("tmpdir")
    logging.info(str(tmpdir))
    # ensure local test created packages can be imported
    sys.path.insert(0, str(tmpdir))
    # Chdir only for the duration of the test.
    with tmpdir.as_cwd():
        yield

def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)
