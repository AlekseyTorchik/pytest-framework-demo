from pytest import mark


# Simple tests stubs
@mark.widget
class WidgetTests:

    def test_widget_functions_as_expected(self):
        assert True

    @mark.xfail(reason="Fail test stub")
    def test_widget_fails(self):
        assert False
