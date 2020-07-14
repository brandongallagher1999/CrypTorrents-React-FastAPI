import React from 'react';


export default class ProfileBar extends React.Component
{

    constructor(props)
    {
        super(props);
    }

    componentDidMount()
    {
        fetch(`api/get/user/`, {    // get the users profile info
            method : "GET",
            credentials : "same-origin"
        })
        .then(response => response.json()) //then is called with response as the argument then we get it's .json
        .then(data => { //this .then() function takes the last functions response as an argument
            this.setState({
                profile : data
            })
        });
    }
    
    render()
    {
        return(
            <div>
                <div className="profile_box"></div>

            <tbody>
                <tr>
                    <td>
                        <strong style="color: black;">
                            {"to fill out"}
                        </strong>
                        
                    </td>
                </tr> 
            </tbody>
            </div>
        
        );
    }

}