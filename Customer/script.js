(function () {
    let app = angular.module('app', []);

    app.controller('loginCtrl', function ($http) {
        let login = this;
        login.submit = () => {
            $http({
                    method: 'POST',
                    url: 'http://90a217506a14.ngrok.io/registration/login/',
                    data: {
                        "email": login.email,
                        "password": login.password
                    }
                })
                .then(
                    mysuccess = (response) => {
                        console.log(response.data)
                        sessionStorage.name = response[0].name;
                        sessionStorage.email = response[0].email;
                        sessionStorage.address = response[0].address;
                        sessionStorage.mobile_no = response[0].mobile_no;
                        window.location.href = "homepage/index.html";
                    },
                    myfailure = (response) => {
                        console.log(response)
                    }
                )
        }
    })

    app.controller('registrationCtrl', function ($http) {
        let reg = this;
        reg.submit = () => {
            console.log(reg)
            $http({
                    method: 'POST',
                    url: 'http://90a217506a14.ngrok.io/registration/',
                    data: {
                        "name": reg.name,
                        "email": reg.email,
                        "password": reg.password,
                        "mobile_no": reg.mobile_no
                    }
                })
                .then(
                    mysuccess = (response) => {
                        console.log(response)
                        if (response.data == "Registered Sucessfully") {
                            sessionStorage.email = reg.email;
                            sessionStorage.password = reg.password;
                            $http({
                                    method: 'POST',
                                    url: 'http://90a217506a14.ngrok.io/registration/login/',
                                    data: {
                                        "email": reg.email,
                                        "password": reg.password
                                    }
                                })
                                .then(
                                    mySuccess = (response) => {
                                        console.log(response)
                                        sessionStorage.name = response[0].name;
                                        sessionStorage.email = response[0].email;
                                        sessionStorage.address = response[0].address;
                                        sessionStorage.mobile_no = response[0].mobile_no;
                                        window.location.href = "homepage/index.html";
                                    },
                                    myFailure = (response) => {
                                        console.log(response.data)
                                    }
                                )
                        }
                    },
                    myfailure = (response) => {
                        console.log(response)
                    }
                )
        }
    })
})();