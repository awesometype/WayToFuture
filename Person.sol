pragma solidity ^0.4.23;

contract Person{
    uint64 _age;
    uint64 _height;
    address _owner;
    
    constructor() public{
        _age = 23;
        _height = 180;
        _owner = msg.sender;
    }
    
    function setAge(uint64 age) public{
        _age = age;
    }
    
    function age() 
        public constant
        returns(uint64) 
    {
        return _age;
    }
    
    function kill() public{
        if(_owner == msg.sender){
            selfdestruct(_owner);
        }
    }
    
    
}
