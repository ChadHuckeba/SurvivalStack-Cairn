import logging
from cairn import Cairn, get_logger, cairn_test_context

def test_cairn_initialization(tmp_path):
    log_file = tmp_path / "test.log"
    Cairn.initialize(project_name="TestProject", log_file=str(log_file), level="DEBUG")
    
    logger = get_logger("test_logger")
    logger.debug("Test message")
    
    # Check if file exists
    assert log_file.exists()
    
    # Check content
    content = log_file.read_text()
    assert "[DEBUG]" in content
    assert "[TestProject]" in content
    assert "test_logger" in content
    assert "Test message" in content
    
    Cairn.reset()

def test_test_context():
    Cairn.initialize(project_name="ContextProject", level="INFO")
    assert logging.getLogger().level == logging.INFO
    
    with cairn_test_context(level="DEBUG"):
        assert logging.getLogger().level == logging.DEBUG
        
    assert logging.getLogger().level == logging.INFO
    Cairn.reset()
