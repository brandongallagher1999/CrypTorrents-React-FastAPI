import React from 'react';
import Torrent from './Torrent';
import '../Styles/style.css'

export default class TorrentTable extends React.Component
{
    constructor(props)
    {
        super(props);
        this.state = {
            torrents : []
        };
    }

    componentDidMount()
    {
        console.log("HI!!!");
        let torrent_string = window.location.href.split("/")[4];
        console.log(window.location.href);

        fetch(`http://localhost:8000/api/torrents/get/${torrent_string}`, {
            headers : {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        })
        .then(res => res.json())
        .then(data => {
            this.setState({
                torrents : data
            })
        });
        
    }

    render()
    {

        return(
            <table className="table" style={{ position: "relative", top : "25px", width : "100%"}}>
                <thead>
                    <tr>
                        <th scope="col">
                            
                        </th>

                        <th scope="col">
                            Torrent Name
                        </th>

                        <th scope="col">
                            Magnet
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {
                        this.state.torrents.map(torrent => {
                            return <Torrent name={torrent.name} magnet={torrent.magnet} image={torrent.image_url}/>
                        })
                    }
                </tbody>
            </table>
        );
    }
}