from endstone import Plugin

class WaffenLib(Plugin):
    def on_enable(self) -> None:
        self.get_logger().info("§aWaffenLib v0.1.0 загружена!")

    def on_disable(self) -> None:
        self.get_logger().info("§cWaffenLib выгружена.")