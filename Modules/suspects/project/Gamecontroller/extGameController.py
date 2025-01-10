'''Info Header Start
Name : extGameController
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12000
Info Header End'''

from typing import Literal
from collections import Counter

class extGameController:
	"""
	Handles the gamelogic and infers the current state of the game.
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	@property
	def GameData(self):
		return iop.Store.Gamedata
	
	@property
	def GameBoard(self) -> tableDAT:
		return self.GameData.op("gameBoard")
	
	def Set(self, xIndex:int, yIndex:int):
		if not self._set( xIndex, yIndex, iop.Store.Datastore.par.Activeplayer.eval()): 
			iop.Store.Emitter.Emit("InvalidGameoption", "Spot already taken.")
			return
		iop.Store.Emitter.Emit("Set")
		self.nextPlayer()
	
	def nextPlayer(self):
		iop.Store.Datastore.par.Activeplayer.menuIndex = (iop.Store.Datastore.par.Activeplayer.menuIndex + 1) % len( iop.Store.Datastore.par.Activeplayer.menuNames)


	def _set(self, xIndex:int, yIndex:int, value:Literal["X", "O"]):
		cell = self.GameBoard[xIndex, yIndex]
		if cell.val: return False
		cell.val = value
		return True
	
	def Reset(self):
		for row in self.GameBoard.rows():
			for cell in row:
				cell.val = ""

	@property
	def Winner(self):
		for streak in (
			self.GameBoard.rows() + 
			self.GameBoard.cols() + 
			[ [self.GameBoard[rowIndex, colIndex] for rowIndex, colIndex in zip(
				range(0, self.GameBoard.numRows ), range(0, self.GameBoard.numCols ), 
			)] , 
			[self.GameBoard[rowIndex, colIndex] for rowIndex, colIndex in zip(
				range(self.GameBoard.numRows,0 ), range(self.GameBoard.numCols,0 ), 
			)]]
			):
			result = Counter([cell.val for cell in streak])
			
			if ( result 
	   				and len( result ) > 0 
					and list(result.values())[0] < self.GameBoard.numRows) : 
				continue
			
			return list(result.keys())[0]
			 
			