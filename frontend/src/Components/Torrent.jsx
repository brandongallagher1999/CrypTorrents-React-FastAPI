import React from 'react';

export default class Torrent extends React.Component
{
    constructor(props)
    {
        super(props);
    }
    

    displayMagnet()
    {
        /*
        Displays the magnet box that is Copyable.
        */
        prompt("Copy this with CTRL + C", this.props.magnet);
    }

    //Props = name, magnet, size, category
    render()
    {
        const {name, image} = this.props;
        const divStyle = {
            backgroundImage : `url(${image})`,
            width: "200px",
            height: "200px"
        };
        
        return(
            <tr>
                <td>
                    <div style={divStyle}>
                    </div>
                </td>
                <td>
                    <strong style={{ color: 'black'}}>
                        {name}
                    </strong>
                    
                </td>
                <td>
                    <button className="pirate_icon" onClick={this.displayMagnet.bind(this)}>
                    </button>
                </td>
            </tr>
        );
    }
}
