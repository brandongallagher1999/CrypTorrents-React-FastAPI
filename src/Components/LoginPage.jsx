import React from 'react';

export default class LoginPage extends React.Component
{
    constructor(props)
    {
        super(props);
        this.state = {};
    };

    async submitLogin()
    {
        let username = document.getElementById("username_input1").value;
        let password = document.getElementById("password_input1").value;

        let data = {
            "username": username,
            "password": password
        };  
        
        let url = "/sessions/login/";
        const req = await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': "application/json",
                "Accept" : "application/json",
            },
            body: JSON.stringify(data)
        });
    };

    render()
    {
        const divStyle = {
            top : "25%",
            position: "absolute",
            left: "30%",
            width: "650px",
            height: "auto",
            backgroundColor : "whitesmoke",
            borderRadius: "25px",
        };

        return(
            <form>
                <div style={divStyle}>
                    <div style={{margin: "30px"}}>
                            <label htmlFor="username_input1">Username</label>
                            <input type="text" className="input is-primary" id="username_input1" placeholder="Ex. username123"/>
                            <label htmlFor="password_input1">Password</label>
                            <input type="password" className="input is-primary" id="password_input1" placeholder=""/>
                            <button type="submit" href={null} className="button is-primary" id="login_submission" style={{top: "10px"}} onClick={this.submitLogin.bind(this)}>Submit</button>
                            <small id="password_help" style={{position: "relative", left: "20px", top: "20px"}}className="form-text text-muted">If you forgot your password click <a href="">here</a></small>
                    </div>
                </div>
            </form>
        );
    };

}