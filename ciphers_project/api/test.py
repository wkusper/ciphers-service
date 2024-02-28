from ciphers_project.api.ciphers import caesar_encode


def test_caesar_encode():
    # Test with shift of 3
    assert caesar_encode("hello", 3) == "khoor"
    
    # Test with shift of 5
    assert caesar_encode("world", 5) == "btwqi"
    
    # Test with shift of 0 (no change expected)
    assert caesar_encode("hello", 0) == "hello"
    
    # Test with negative shift
    assert caesar_encode("world", -2) == "umqjb"
    
    # Test with large shift (wrap around expected)
    assert caesar_encode("hello", 30) == "lipps"
    
    # Test with non-alphabetic characters
    assert caesar_encode("hello, world!", 3) == "khoor, zruog!"
    
    print("All tests passed!")

# Run the test cases
test_caesar_encode()

def test_caesar_encode():
    # Test with shift of 1
    assert caesar_encode("abc", 1) == "bcd"
    
    # Test with shift of 13 (rot13)
    assert caesar_encode("hello", 13) == "uryyb"
    
    # Test with shift of 26 (same as shift of 0)
    assert caesar_encode("world", 26) == "world"
    
    # Test with shift of -5
    assert caesar_encode("abc", -5) == "vwx"
    
    # Test with shift of 25
    assert caesar_encode("xyz", 25) == "wxy"
    
    # Test with empty string
    assert caesar_encode("", 5) == ""
    
    print("All tests passed!")

# Run the test cases
test_caesar_encode()

