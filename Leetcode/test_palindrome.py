from validPalindrome import validPalindrome

def test_chuoi_doi_xung_chuan():
    assert validPalindrome("abccba") == True
    assert validPalindrome("racecar") == True
    assert validPalindrome("a") == True
    assert validPalindrome("") == True

def test_chuoi_sai():
    assert validPalindrome("abc") == False
    assert validPalindrome("abcd") == False
    assert validPalindrome("abccaa") == False

def test_chuoi_xoa_mot_ki_tu():
    assert validPalindrome("abca") == True
    assert validPalindrome("racecarx") == True
    assert validPalindrome("aabbcc") == True

def test_chuoi_rong():
    assert validPalindrome("") == True

