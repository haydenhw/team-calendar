import React from 'react';

import FormControl from '@material-ui/core/FormControl';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';

class TextInput extends React.Component {
    render () {
        const { label, handleChange, type }  = this.props;

        return (
            <FormControl margin="normal" fullWidth>
                <InputLabel>{label}</InputLabel>
                <Input onChange={handleChange} autoFocus type={type}/>
            </FormControl>
        );

    }
}

export default TextInput;

