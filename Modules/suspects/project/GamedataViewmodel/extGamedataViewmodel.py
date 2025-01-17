'''Info Header Start
Name : extGamedataViewmodel
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12000
Info Header End'''

from typing import Literal
from collections import Counter

class extGamedataViewmodel:
	"""
	extGamedataViewmodel description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.AvailablePlayer = iop.Store.Gamedata.par.Availableplayer
		self.ActivePlayer = iop.Store.Gamedata.par.Activeplayer


	@property
	def GameData(self):
		return iop.Store.Gamedata
	
	@property
	def GameBoard(self) -> tableDAT:
		return self.GameData.op("gameBoard")

	@property
	def NumTurns(self):
		return len( [ cell.val for cell in self.GameBoard.cells("*", "*") if cell.val])

	
	@property
	def Winner(self):
		if self.NumTurns >= self.GameBoard.numCols * self.GameBoard.numRows : return "DRAW"
		
		for streak in (
			self.GameBoard.rows() + 
			self.GameBoard.cols() + 
			[ [self.GameBoard[rowIndex, colIndex] for rowIndex, colIndex in zip(
				range(0, self.GameBoard.numRows ), range(0, self.GameBoard.numCols ), 
			)] , 
			[self.GameBoard[rowIndex, colIndex] for rowIndex, colIndex in zip(
				range(0, self.GameBoard.numRows), range(self.GameBoard.numCols-1,-1,-1 ), 
			)]]
			):
			result = Counter([cell.val for cell in streak])
			debug( result )
			if (not result) : return ""
			if ( len( result ) > 0 
					and list(result.values())[0] < self.GameBoard.numRows) : 
				continue
			
			return list(result.keys())[0]
		return ""
			 
