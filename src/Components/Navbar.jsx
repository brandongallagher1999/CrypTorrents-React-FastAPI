
import React from 'react';


export default class NavBar extends React.Component
{
    constructor(props)
    {
        super(props);
    };

    render()
    {
        return(
            <nav className="navbar" role="navigation" aria-label="main navigation">
                <div className="navbar-brand">
                    <a className="navbar-item" href="/">
                    <img src="https://img.favpng.com/22/25/6/jolly-roger-piracy-logo-clip-art-png-favpng-nK62hAPB2fQt7fZFcfMi2Vtuw.jpg" width="112" height="28"></img>
                    </a>
                
                </div>
                
                <div id="navbarBasicExample" className="navbar-menu">
                    <div className="navbar-start">
                    <a className="navbar-item" href="/">
                        <strong>Home</strong>
                    </a>
                
                    <a className="navbar-item" href="https://github.com/brandongallagher1999/CrypTorrents---FastAPI">
                        <strong>Documentation</strong>
                    </a>
                </div>
                <div className="navbar-end">
                    <div className="navbar-item">
                        <div className="buttons">
                        <button className="button is-primary" disabled>
                            <strong>Join</strong>
                        </button>
                        <button className="button is-light" href="/tests/1" disabled>
                            <strong>Log In</strong>
                        </button>
                        </div>
                    </div>
                    </div>
                </div>
            </nav>

        );
    };
}