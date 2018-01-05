#------------------------------------Close Other Windows ----------------------
# Author: Manfred Wuits
# Email : manfred@werkzeugh.at
# Version : 1.0
#----------------------------------------------------------------------------

import sublime, sublime_plugin
        
class closeOtherWindowsCommand(sublime_plugin.WindowCommand):
    def run(self):
        allWindows=sublime.windows()
        currentWindow = sublime.active_window()
        for i,w in enumerate(allWindows):
            if currentWindow != w:
                w.run_command('close_window')


class closeOtherTabsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        group_index, view_index = window.get_view_index(self.view)
        window.run_command("close_others_by_index", {"group": group_index, "index": view_index})


class closeTabsToTheRightCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        group_index, view_index = window.get_view_index(self.view)
        window.run_command("close_to_right_by_index", {"group": group_index, "index": view_index})
