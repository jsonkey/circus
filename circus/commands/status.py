from circus.commands.base import Command
from circus.exc import ArgumentError, MessageError

class Status(Command):
    """Get the status of a show or all shows"""

    name = "status"

    def message(self, *args, **opts):
        if len(args) > 1:
            raise ArgumentError("message invalid")

        if len(args) == 1:
            return self.make_message(name=args[0])
        else:
            return self.make_message()

    def execute(self, trainer, props):
        if 'name' in props:
            show = self._get_show(trainer, props['name'])
            return {"status": show.status()}
        else:
            return {"statuses": trainer.statuses()}

    def console_msg(self, msg):
        if "statuses" in msg:
            statuses = msg.get("statuses")
            shows = sorted(statuses)
            return "\n".join(["%s: %s" % (show, statuses[show]) \
                    for show in shows])
        elif "status" in msg and status != "error":
            return msg.get("status")
        return self.console_error(msg)