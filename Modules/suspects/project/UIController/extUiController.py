'''Info Header Start
Name : extUiController
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12000
Info Header End'''


class extUiController:
	"""
	Handles the UI, stuff like state transitions and the like.
	Has not inherent use for the beginning.
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.compositor = self.ownerComp.op("SceneCompositor")

	