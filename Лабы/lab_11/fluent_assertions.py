class FluentAssertions:
    @staticmethod
    def assert_equal(actual, expected, message=""):
        assert actual == expected, message

    @staticmethod
    def assert_not_none(value, message=""):
        assert value is not None, message

    @staticmethod
    def assert_contains(item, collection, message=""):
        assert item in collection, message
