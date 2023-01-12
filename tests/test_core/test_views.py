def test_robots_txt(client):
    response = client.get("/robots.txt")

    assert b"User-agent: *" in response.content
