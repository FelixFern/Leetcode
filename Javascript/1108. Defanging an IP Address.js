var defangIPaddr = function (address) {
    console.log(address.replaceAll(".", "[.]"));
};

defangIPaddr("1.1.1.1");
