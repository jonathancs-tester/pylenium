def test_google_search(py):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies')
    py.get("[name='btnK']").submit()
    assert 'puppies' in py.title                                                                                                                     def test_google_search(py):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies')
    py.get("[name='btnK']").submit()
    assert 'puppies' in py.title