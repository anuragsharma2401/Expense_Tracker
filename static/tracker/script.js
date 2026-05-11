function validForm(){
    var u = document.forms["myform"]["username"].value;
    var fn = document.forms["myform"]["first_name"].value;
    var ln = document.forms["myform"]["last_name"].value;
    var pwd = document.forms["myform"]["password"].value;

    if (u == ""){
        alert("Username can't be empty")
        return false
    }
    if(u.length<3)
    {
        alert("Username must be at least 3 characters long.")
        return false
    }
    if (fn == ""){
        alert("First name can't be empty")
        return false
    }
    let namepattern=/^[A-Za-z\s]+$/;
    if (!namepattern.test(fn)){
        alert("First name can only contain letters and spaces.")
        return false
    }
    
    if (ln == ""){
        alert("Last name can't be empty")
        return false
    }

    if (!namepattern.test(ln)){
        alert("Last name can only contain letters and spaces.")
        return false
    }
    if (pwd == ""){
        alert("Password can't be empty")
        return false
    }
}