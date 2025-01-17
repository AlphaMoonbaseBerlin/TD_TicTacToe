
'''Info Header Start
Name : extUiLogic
Author : Wieland@AMB-ZEPH15
Saveorigin : TicTacToe.toe
Saveversion : 2023.12000
Info Header End'''


class extUiLogic:
	"""
	extUiLogic description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def AknowledgeWinner(self):
		iop.Store.Datastore.par.Winneraknowledged.pulse( frames = 4)
		return
	
	def SelectPlayer(self, playerCharacter):
		iop.Store.Gamecontroller.PickPlayer( playerCharacter )

		return
	
	def Set(self, row, col):
		iop.Store.Gamecontroller.Set(
			row, col
		)
		return