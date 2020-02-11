import React from 'react';
import ReactDOM from 'react-dom';
import App from '../src/App';
import Enzyme, { mount, shallow } from 'enzyme';

describe('Render tests', () => {
    it('renders without crashing', () => {
        const div = document.createElement('div');
        ReactDOM.render(<App />, div);
        ReactDOM.unmountComponentAtNode(div);
    });
    it('Shows Setsuwa title', () => {
        const wrapper = shallow(<App />);
        const text = wrapper.find('h1');
        expect(text.text()).toEqual("Setsuwa");
    });
    it('Shows home & login/register when logged out', () => {
        const wrapper = shallow(<App />);
        wrapper.setState({loggedIn: false});
        let link = wrapper.find('Link');
        expect(link.length).toEqual(2);
    });
    it('Shows login/register when logged out', () => {
        const wrapper = shallow(<App />);
        wrapper.setState({loggedIn: false});
        let link = wrapper.find('#login');
        expect(link.text()).toEqual("Login/Register");
    });
    it('Shows more options in nav bar when logged in', () => {
        const wrapper = shallow(<App />);
        wrapper.setState({loggedIn: true});
        let link = wrapper.find('Link');
        expect(link.length).toEqual(5);
    });
    it('Shows login/register when logged out', () => {
        const wrapper = shallow(<App />);
        wrapper.setState({loggedIn: true});
        let link = wrapper.find('#logout');
        expect(link.text()).toEqual("Logout");
    })
})