from roschat_app.console_ui_elements import ScrollingTextField


class FakeConsole:
    def __init__(self):
        self.drawn = []

    def register_update_callback(self, _callback):
        self.registered_callback = _callback
        return 0

    def draw_string(self, x, y, text, _fg, _bg, maxLen):
        self.drawn.append((x, y, text, maxLen, _fg, _bg))


def rendered_lines(field, console):
    console.drawn.clear()
    field.update()
    return [draw[2] for draw in console.drawn]


def test_wraps_and_starts_at_bottom():
    console = FakeConsole()
    field = ScrollingTextField(console, 2, 3, 4, 2, "abcdefghij")

    assert rendered_lines(field, console) == ["efgh", "ij"]


def test_scroll_offset_tracks_appended_wrapped_lines():
    console = FakeConsole()
    field = ScrollingTextField(console, 0, 0, 4, 2, "abcdefghijkl")
    field.scroll_up(1)
    assert rendered_lines(field, console) == ["abcd", "efgh"]

    field.append_text("mn")

    assert field.scroll_offset == 2
    assert rendered_lines(field, console) == ["abcd", "efgh"]


def test_scrolling_controls_visibility_and_text_changes():
    console = FakeConsole()
    field = ScrollingTextField(console, 0, 0, 3, 2, "abcdefghi")

    field.disable_scrolling()
    field.scroll_up()
    assert field.scroll_offset == 0
    field.enable_scrolling()
    field.scroll_up(10)
    assert field.scroll_offset == 1
    field.scroll_down()
    assert field.scroll_offset == 0

    field.hide()
    assert rendered_lines(field, console) == []
    field.show()
    assert rendered_lines(field, console) == ["def", "ghi"]

    field.change_text("a\nb")
    assert field.scroll_offset == 0
    assert rendered_lines(field, console) == ["a", "b"]

    field.clear_text()
    assert field.scroll_offset == 0
    assert rendered_lines(field, console) == [""]
