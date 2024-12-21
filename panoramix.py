# Palkeoramix decompiler. 

const decimals = 18

def storage:
  balanceOf is mapping of uint256 at storage 0
  allowance is mapping of uint256 at storage 1
  totalSupply is uint256 at storage 2
  stor3 is array of struct at storage 3
  stor4 is array of struct at storage 4
  owner is addr at storage 5

def totalSupply() payable: 
  return totalSupply

def balanceOf(address _owner) payable: 
  require calldata.size - 4 >=ΓÇ▓ 32
  require _owner == _owner
  return balanceOf[addr(_owner)]

def owner() payable: 
  return owner

def allowance(address _owner, address _spender) payable: 
  require calldata.size - 4 >=ΓÇ▓ 64
  require _owner == _owner
  require _spender == _spender
  return allowance[addr(_owner)][addr(_spender)]

#
#  Regular functions
#

def _fallback() payable: # default function
  revert

def renounceOwnership() payable: 
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  owner = 0
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)

def transferOwnership(address _newOwner) payable: 
  require calldata.size - 4 >=ΓÇ▓ 32
  require _newOwner == _newOwner
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  if not _newOwner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Ownable: new owner is the zero address'
  owner = _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)

def mint(address _to, uint256 _amount) payable: 
  require calldata.size - 4 >=ΓÇ▓ 64
  require _to == _to
  require _amount == _amount
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  if not _to:
      revert with 0, 'ERC20: mint to the zero address'
  if totalSupply > -_amount - 1:
      revert with 'NH{q', 17
  totalSupply += _amount
  balanceOf[addr(_to)] += _amount
  log Transfer(
        address from=_amount,
        address to=0,
        uint256 tokens=_to)

def approve(address _spender, uint256 _value) payable: 
  require calldata.size - 4 >=ΓÇ▓ 64
  require _spender == _spender
  require _value == _value
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve from the zero address'
  if not _spender:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve to the zero address'
  allowance[caller][addr(_spender)] = _value
  log Approval(
        address tokenOwner=_value,
        address spender=caller,
        uint256 tokens=_spender)
  return 1

def burn(address _guy, uint256 _wad) payable: 
  require calldata.size - 4 >=ΓÇ▓ 64
  require _guy == _guy
  require _wad == _wad
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  if not _guy:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: burn from the zero address'
  if balanceOf[addr(_guy)] < _wad:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: burn amount exceeds balance'
  balanceOf[addr(_guy)] -= _wad
  totalSupply -= _wad
  log Transfer(
        address from=_wad,
        address to=_guy,
        uint256 tokens=0)

def transfer(address _to, uint256 _value) payable: 
  require calldata.size - 4 >=ΓÇ▓ 64
  require _to == _to
  require _value == _value
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer from the zero address'
  if not _to:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer to the zero address'
  if balanceOf[caller] < _value:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer amount exceeds balance'
  balanceOf[caller] -= _value
  balanceOf[addr(_to)] += _value
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 tokens=_to)
  return 1

def increaseAllowance(address _spender, uint256 _addedValue) payable: 
  require calldata.size - 4 >=ΓÇ▓ 64
  require _spender == _spender
  require _addedValue == _addedValue
  if allowance[caller][addr(_spender)] > -_addedValue - 1:
      revert with 'NH{q', 17
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve from the zero address'
  if not _spender:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve to the zero address'
  allowance[caller][addr(_spender)] += _addedValue
  log Approval(
        address tokenOwner=(allowance[caller][addr(_spender)] + _addedValue),
        address spender=caller,
        uint256 tokens=_spender)
  return 1

def decreaseAllowance(address _spender, uint256 _subtractedValue) payable: 
  require calldata.size - 4 >=ΓÇ▓ 64
  require _spender == _spender
  require _subtractedValue == _subtractedValue
  if allowance[caller][addr(_spender)] < _subtractedValue:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: decreased allowance below zero'
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve from the zero address'
  if not _spender:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve to the zero address'
  allowance[caller][addr(_spender)] -= _subtractedValue
  log Approval(
        address tokenOwner=(allowance[caller][addr(_spender)] - _subtractedValue),
        address spender=caller,
        uint256 tokens=_spender)
  return 1

def transferFrom(address _from, address _to, uint256 _value) payable: 
  require calldata.size - 4 >=ΓÇ▓ 96
  require _from == _from
  require _to == _to
  require _value == _value
  if allowance[addr(_from)][caller] != -1:
      if allowance[addr(_from)][caller] < _value:
          revert with 0, 'ERC20: insufficient allowance'
      if not _from:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve from the zero address'
      if not caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve to the zero address'
      allowance[addr(_from)][caller] -= _value
      log Approval(
            address tokenOwner=(allowance[addr(_from)][caller] - _value),
            address spender=_from,
            uint256 tokens=caller)
  if not _from:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer from the zero address'
  if not _to:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer to the zero address'
  if balanceOf[addr(_from)] < _value:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer amount exceeds balance'
  balanceOf[addr(_from)] -= _value
  balanceOf[addr(_to)] += _value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 tokens=_to)
  return 1

def airdrop(address[] _participants, uint256 _totalAmount) payable: 
  require calldata.size - 4 >=ΓÇ▓ 64
  require _participants <= 18446744073709551615
  require _participants + 35 <ΓÇ▓ calldata.size
  require _participants.length <= 18446744073709551615
  require _participants + (32 * _participants.length) + 36 <= calldata.size
  require _totalAmount == _totalAmount
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  idx = 0
  while idx < _participants.length:
      require cd[((32 * idx) + _participants + 36)] == addr(cd[((32 * idx) + _participants + 36)])
      if not caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer from the zero address'
      if not addr(cd[((32 * idx) + _participants + 36)]):
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer to the zero address'
      if balanceOf[caller] < _totalAmount:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer amount exceeds balance'
      balanceOf[caller] -= _totalAmount
      mem[0] = addr(cd[((32 * idx) + _participants + 36)])
      mem[32] = 0
      balanceOf[addr(cd[((32 * idx) + _participants + 36)])] += _totalAmount
      mem[96] = _totalAmount
      log Transfer(
            address from=_totalAmount,
            address to=caller,
            uint256 tokens=addr(cd[((32 * idx) + _participants + 36)]))
      if idx == -1:
          revert with 'NH{q', 17
      idx = idx + 1
      continue 

def name() payable: 
  if bool(stor3.length):
      if bool(stor3.length) == stor3.length.field_1 < 32:
          revert with 'NH{q', 34
      if bool(stor3.length):
          if bool(stor3.length) == stor3.length.field_1 < 32:
              revert with 'NH{q', 34
          if stor3.length.field_1:
              if 31 < stor3.length.field_1:
                  mem[128] = uint256(stor3.field_0)
                  idx = 128
                  s = 0
                  while stor3.length.field_1 + 96 > idx:
                      mem[idx + 32] = stor3[s].field_256
                      idx = idx + 32
                      s = s + 1
                      continue 
                  return Array(len=2 * Mask(256, -1, stor3.length.field_1), data=mem[128 len ceil32(stor3.length.field_1)])
              mem[128] = 256 * stor3.length.field_8
      else:
          if bool(stor3.length) == stor3.length.field_1 < 32:
              revert with 'NH{q', 34
          if stor3.length.field_1:
              if 31 < stor3.length.field_1:
                  mem[128] = uint256(stor3.field_0)
                  idx = 128
                  s = 0
                  while stor3.length.field_1 + 96 > idx:
                      mem[idx + 32] = stor3[s].field_256
                      idx = idx + 32
                      s = s + 1
                      continue 
                  return Array(len=2 * Mask(256, -1, stor3.length.field_1), data=mem[128 len ceil32(stor3.length.field_1)])
              mem[128] = 256 * stor3.length.field_8
      mem[ceil32(stor3.length.field_1) + 192 len ceil32(stor3.length.field_1)] = mem[128 len ceil32(stor3.length.field_1)]
      if ceil32(stor3.length.field_1) > stor3.length.field_1:
          mem[ceil32(stor3.length.field_1) + stor3.length.field_1 + 192] = 0
      return Array(len=2 * Mask(256, -1, stor3.length.field_1), data=mem[128 len ceil32(stor3.length.field_1)], mem[(2 * ceil32(stor3.length.field_1)) + 192 len 2 * ceil32(stor3.length.field_1)]), 
  if bool(stor3.length) == stor3.length.field_1 < 32:
      revert with 'NH{q', 34
  if bool(stor3.length):
      if bool(stor3.length) == stor3.length.field_1 < 32:
          revert with 'NH{q', 34
      if stor3.length.field_1:
          if 31 < stor3.length.field_1:
              mem[128] = uint256(stor3.field_0)
              idx = 128
              s = 0
              while stor3.length.field_1 + 96 > idx:
                  mem[idx + 32] = stor3[s].field_256
                  idx = idx + 32
                  s = s + 1
                  continue 
              return Array(len=stor3.length % 128, data=mem[128 len ceil32(stor3.length.field_1)])
          mem[128] = 256 * stor3.length.field_8
  else:
      if bool(stor3.length) == stor3.length.field_1 < 32:
          revert with 'NH{q', 34
      if stor3.length.field_1:
          if 31 < stor3.length.field_1:
              mem[128] = uint256(stor3.field_0)
              idx = 128
              s = 0
              while stor3.length.field_1 + 96 > idx:
                  mem[idx + 32] = stor3[s].field_256
                  idx = idx + 32
                  s = s + 1
                  continue 
              return Array(len=stor3.length % 128, data=mem[128 len ceil32(stor3.length.field_1)])
          mem[128] = 256 * stor3.length.field_8
  mem[ceil32(stor3.length.field_1) + 192 len ceil32(stor3.length.field_1)] = mem[128 len ceil32(stor3.length.field_1)]
  if ceil32(stor3.length.field_1) > stor3.length.field_1:
      mem[ceil32(stor3.length.field_1) + stor3.length.field_1 + 192] = 0
  return Array(len=stor3.length % 128, data=mem[128 len ceil32(stor3.length.field_1)], mem[(2 * ceil32(stor3.length.field_1)) + 192 len 2 * ceil32(stor3.length.field_1)]), 

def symbol() payable: 
  if bool(stor4.length):
      if bool(stor4.length) == stor4.length.field_1 < 32:
          revert with 'NH{q', 34
      if bool(stor4.length):
          if bool(stor4.length) == stor4.length.field_1 < 32:
              revert with 'NH{q', 34
          if stor4.length.field_1:
              if 31 < stor4.length.field_1:
                  mem[128] = uint256(stor4.field_0)
                  idx = 128
                  s = 0
                  while stor4.length.field_1 + 96 > idx:
                      mem[idx + 32] = stor4[s].field_256
                      idx = idx + 32
                      s = s + 1
                      continue 
                  return Array(len=2 * Mask(256, -1, stor4.length.field_1), data=mem[128 len ceil32(stor4.length.field_1)])
              mem[128] = 256 * stor4.length.field_8
      else:
          if bool(stor4.length) == stor4.length.field_1 < 32:
              revert with 'NH{q', 34
          if stor4.length.field_1:
              if 31 < stor4.length.field_1:
                  mem[128] = uint256(stor4.field_0)
                  idx = 128
                  s = 0
                  while stor4.length.field_1 + 96 > idx:
                      mem[idx + 32] = stor4[s].field_256
                      idx = idx + 32
                      s = s + 1
                      continue 
                  return Array(len=2 * Mask(256, -1, stor4.length.field_1), data=mem[128 len ceil32(stor4.length.field_1)])
              mem[128] = 256 * stor4.length.field_8
      mem[ceil32(stor4.length.field_1) + 192 len ceil32(stor4.length.field_1)] = mem[128 len ceil32(stor4.length.field_1)]
      if ceil32(stor4.length.field_1) > stor4.length.field_1:
          mem[ceil32(stor4.length.field_1) + stor4.length.field_1 + 192] = 0
      return Array(len=2 * Mask(256, -1, stor4.length.field_1), data=mem[128 len ceil32(stor4.length.field_1)], mem[(2 * ceil32(stor4.length.field_1)) + 192 len 2 * ceil32(stor4.length.field_1)]), 
  if bool(stor4.length) == stor4.length.field_1 < 32:
      revert with 'NH{q', 34
  if bool(stor4.length):
      if bool(stor4.length) == stor4.length.field_1 < 32:
          revert with 'NH{q', 34
      if stor4.length.field_1:
          if 31 < stor4.length.field_1:
              mem[128] = uint256(stor4.field_0)
              idx = 128
              s = 0
              while stor4.length.field_1 + 96 > idx:
                  mem[idx + 32] = stor4[s].field_256
                  idx = idx + 32
                  s = s + 1
                  continue 
              return Array(len=stor4.length % 128, data=mem[128 len ceil32(stor4.length.field_1)])
          mem[128] = 256 * stor4.length.field_8
  else:
      if bool(stor4.length) == stor4.length.field_1 < 32:
          revert with 'NH{q', 34
      if stor4.length.field_1:
          if 31 < stor4.length.field_1:
              mem[128] = uint256(stor4.field_0)
              idx = 128
              s = 0
              while stor4.length.field_1 + 96 > idx:
                  mem[idx + 32] = stor4[s].field_256
                  idx = idx + 32
                  s = s + 1
                  continue 
              return Array(len=stor4.length % 128, data=mem[128 len ceil32(stor4.length.field_1)])
          mem[128] = 256 * stor4.length.field_8
  mem[ceil32(stor4.length.field_1) + 192 len ceil32(stor4.length.field_1)] = mem[128 len ceil32(stor4.length.field_1)]
  if ceil32(stor4.length.field_1) > stor4.length.field_1:
      mem[ceil32(stor4.length.field_1) + stor4.length.field_1 + 192] = 0
  return Array(len=stor4.length % 128, data=mem[128 len ceil32(stor4.length.field_1)], mem[(2 * ceil32(stor4.length.field_1)) + 192 len 2 * ceil32(stor4.length.field_1)]), 


