pragma solidity 0.4.23;

contract Adoption{
    address[16] public adopters;//保存领养者的地址

    //领养宠物
    function adopt(uint petID) public returns (uint) {
        require(petID >= 0 && petID <= 15);
        adopters[petID] = msg.sender;
        return petID;
    }

    //返回领养者
    function getAdopters() public view returns (address[16]) {
        return adopters;
    }
}
