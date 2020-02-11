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
})
