import React, { Component } from 'react'

export default class WelcomeJumbatron extends Component {

    handleClick = () => {
        const URL = 'http://localhost:8000/authorize/' + this.props.client_id;

        fetch(URL, {
            method: 'GET'
        })
        .then(resp => {
            // Get our `next` url
            document.location.href = resp.url
        })
        .catch(errors => {
            console.log(errors)
        })
    }

    render() {
        return (
            <div className='jumbotron'>
                <h1 className='display-4'>Welcome to Business App</h1>
                <p className='lead'>It is created to test OAuth authentication</p>
                <p>To start working, please login or signup</p>
                <button className="btn btn-success btn-lg login-btn" onClick={this.handleClick}>Login</button>
            </div>
        )
    }
}