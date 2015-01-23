#------------------------------------Close All But This----------------------
# Author: Manfred Wuits
# Email : manfred@werkzeugh.at
# Version : 1.0
#----------------------------------------------------------------------------

import sublime, sublime_plugin
        
class closeowCommand(sublime_plugin.WindowCommand):
    def run(self):
        allWindows=sublime.windows()
        currentWindow = sublime.active_window()
        for i,w in enumerate(allWindows):
            if currentWindow != w:
                w.run_command('close_window')
            
