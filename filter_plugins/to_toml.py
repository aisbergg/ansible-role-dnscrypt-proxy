import toml


class FilterModule(object):

    def filters(self):
        return {
            "to_toml": self.to_toml,
        }

    def to_toml(self, value):
        """Convert the value to TOML"""
        return toml.dumps(value)
