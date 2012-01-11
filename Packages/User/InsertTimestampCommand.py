import datetime
import sublime_plugin

class InsertTimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    #generate the timestamp
    timestamp = datetime.datetime.now()

    # for region in the selection (i.e. if you have multiple regions selected, insert the timestamp in all of them)
    for r in self.view.sel():
      # put in the timestamp (if text is selected, it'll be replaced in an intuitive fashion)
      self.view.replace(edit, r, timestamp.strftime("%Y-%m-%d %H:%M:%S"))