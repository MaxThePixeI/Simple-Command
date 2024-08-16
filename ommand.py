import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello world im Max an I from Denmerk in a small city callet Føvling and Im 15")
