import React, { useState } from 'react';
import axios from 'axios';
import Loader from 'react-loader-spinner';

const App = () => {
    const [loading, setLoading] = useState(false);
    const [agree, setAgree] = useState(false);
    const [formData, setFormData] = useState({
        first_name: '',
        email: '',
    });

    const { first_name, email } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });
    const onChecked = e => setAgree(e.target.checked);

    const onSubmit = e => {
        e.preventDefault();

        const config = {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        };

        const body = JSON.stringify({
            email,
            first_name,
            agree 
        });

        const fetchData = async () => {
            setLoading(true);
            try {
                await axios.post(
                    'http://127.0.0.1:8000/api/v1/email-signup/',
                    body,
                    config
                );
            } catch(err) {

            }
            setLoading(false);
        };

        fetchData();
    }

    return (
        <div className='mt-5 d-flex flex-column justify-content-center align-items-center'>
            <h1 className='display-4 mb-5'>Sign Up to our Newsletter!</h1>
            <form onSubmit={e => onSubmit(e)}>
                <div className='form-group mb-3'>
                    <label className='form-label'>
                        First Name:
                    </label>
                    <input
                        className='form-control'
                        type='text'
                        name='first_name'
                        onChange={e => onChange(e)}
                        value={first_name}
                        required
                    />
                </div>
                <div className='form-group mb-3'>
                    <label className='form-label'>
                        Email:
                    </label>
                    <input
                        className='form-control'
                        type='email'
                        name='email'
                        onChange={e => onChange(e)}
                        value={email}
                        required
                    />
                </div>
                <div className='form-group mb-3'>
                    <input
                        className='form-check-input'
                        type='checkbox'
                        name='agree'
                        onChange={e => onChecked(e)}
                        checked={agree}
                        required
                    />
                    <label 
                        className='form-check-label'
                        style={{ marginLeft: '6px' }} 
                        htmlFor='agree'
                    >
                        I agree to the Privacy Policy and Terms of Service
                    </label>
                </div>
                {
                    loading ? (
                        <div className='d-flex justify-content-center align-items-center'>
                            <Loader 
                                type='Oval' 
                                color='#00BFFF' 
                                height={50} 
                                width={50} 
                                timeout={3000}
                            />
                        </div>
                    ) : (
                        <button className='btn btn-success btn-lg'>
                            Sign Up
                        </button>
                    )
                }
            </form>
        </div>
    );
};

export default App;