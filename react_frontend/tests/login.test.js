import React from 'react';
import ReactDOM from 'react-dom';
import Login from '../src/components/Login';
import Enzyme, { mount, shallow } from 'enzyme';

describe('Render tests', () => {
    it('renders without crashing', () => {
        const div = document.createElement('div');
        ReactDOM.render(<Login />, div);
        ReactDOM.unmountComponentAtNode(div);
    });
    it("Shows 'logged in' when logged in", () => {
        let simFn = jest.fn();
        // let simulatedData = {};
        const wrapper = shallow(<Login 
            handleUsername={simFn}
            handlePassword={simFn}
            handleLogin={simFn}
            handleRegister={simFn} 
            loggedInMessage={"Logged in"}
            registerMessage={"User has been created. Now please log in"} />);
        let message = wrapper.find('#loginMsg');
        expect(message.text()).toEqual("Logged in");
    });
    it("Shows 'logged in' when logged in", () => {
        let simFn = jest.fn();
        // let simulatedData = {handleUsername={simFn}, handlePassword={simFn}, handleLogin={simFn}, handleRegister={simFn}, loggedInMessage={loggedInMessage: "Logged in"}, registerMessage={registerMessage: "User has been created. Now please log in"}};
        const wrapper = shallow(<Login 
            handleUsername={simFn}
            handlePassword={simFn}
            handleLogin={simFn}
            handleRegister={simFn} 
            loggedInMessage={"Logged in"}
            registerMessage={"User has been created. Now please log in"} />);
        let message = wrapper.find('#RegisterMsg');
        expect(message.text()).toEqual("User has been created. Now please log in");
    })
})
