class Plant:
	def __init__(self, name, height):
		self.name = name
		self.height = height

	def get_info(self) -> None:
		print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
	def __init__(self, name, height, color) -> None:
		super().__init__(name, height)
		self.colot: str = color

	def get_info(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
	def __init__(self, name, height, color, prize):
		super().__init__(name, height, color)
		self.prize: int = prize

	def get_info(self):
		print(f" {self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize}")


class GardenManager:
	def __init_(self, name: str) -> None:
		self.name = name
		self.get_message()

	def get_message(self) -> None:
		print(f"Added {self.name} to Alice's garden")
	

	class GardenStats:
		def __init__(self, name: str,height: int ) -> None:
			self.name = name
			self.height = height

		def get_status(self) -> None:
			self.height += 1
			print(f"{self.name} grew 1cm")

	
	def create_garden_network(self):
			pass


if __name__ == "__main__":
	pass