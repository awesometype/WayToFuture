pragma solidity ^0.4.23;

import "truffle/Assert.sol"; //truffle公共的库
import "truffle/DeployedAddresses.sol"; //truffle公共的库
import "../contracts/Adoption.sol";

contract TestAdoption {
    Adoption adoption = Adoption(DeployedAddresses.Adoption());

    // 测试 adopt()
    function testUserCanAdoptPet() {
        uint returnedId = adoption.adopt(8); //调用输入参数

        uint expected = 8; //期望的结果

        Assert.equal(returnedId, expected, "Adoption of pet ID 8 should be recorded."); //判断如果没有就抛出异常
    }

    // 单个测试
    function testGetAdopterAddressByPetId() {

        address expected = this;

        address adopter = adoption.adopters(8);

        Assert.equal(adopter, expected, "Owner of pet ID 8 should be recorded.");
    }

    // 所有的测试
    function testGetAdopterAddressByPetIdInArray() {

        address expected = this;

        address[16] memory adopters = adoption.getAdopters();

        Assert.equal(adopters[8], expected, "Owner of pet ID 8 should be recorded.");
    }


}
