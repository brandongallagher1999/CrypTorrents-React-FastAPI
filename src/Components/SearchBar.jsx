import React from 'react';
import $ from 'jquery';

export default class SearchBar extends React.Component
{
    constructor(props)
    {
        super(props);
        this.state = {
            inputStyle : {
                width : "600px",
                height : "50px"
            },
        };
    }

    keyPress(event)
    {
        if (event.key === "Enter")
        {
            document.getElementById("my-btn-search").click();
        }
    }

    go_to_url()
    {
        let url = "/torrents/" + $("#my-form-query").val();
        document.location.href = url;
    }
    
    render()
    {
        return(
            <div className="columns is-centered is-mobile">
                <div className="column is-half">
                    <div className="container" style= {{top : "10px"}}>
                        <input className="input is-primary" type="text" placeholder="Torrent" id="my-form-query" onKeyPress={this.keyPress} tabIndex="0" style={this.state.inputStyle}></input>
                        <button className="button is-black" id="my-btn-search" onClick={this.go_to_url.bind(this)} style={{height : "50px"}}>Search</button>
                    </div>
                </div>
            </div>
        );
    }
}