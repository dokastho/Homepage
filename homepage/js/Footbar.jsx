import PropTypes from 'prop-types';
import React from 'react'

class Footbar extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className='footbar'>
        <div className='footbar-icon'>
          <a href="https://www.linkedin.com/in/dokastho/" className='svg-link'>
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 448 512" focusable="false" class="chakra-icon css-13otjrl" height="4vh" width="4vh" xmlns="http://www.w3.org/2000/svg">
              <path d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z"></path>
            </svg>
          </a>
        </div>
        <div className='footbar-icon'>
          <a href="https://www.github.com/dokastho/" className='svg-link'>
            <svg xmlns="http://www.w3.org/2000/svg" width="4vh" height="4vh" viewBox="0 0 98 96" fill="currentColor">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z" />
            </svg>
          </a>
        </div>
        <div className='footbar-icon'>
          <a href="https://www.instagram.com/dokastho/" className='svg-link'>
            <svg xmlns="http://www.w3.org/2000/svg" width="4vh" height="4vh" viewBox="0 0 16 16" fill="none" role="img" aria-labelledby="a6d963zjlm0ewypikiha7uupea7dukc" class="octicon">
              <title id="a6d963zjlm0ewypikiha7uupea7dukc">Instagram</title>
              <g clip-path="url(#clip0_202_91849)">
                <path d="M4.66536 0C2.0927 0 0 2.09464 0 4.66797V11.3346C0 13.9073 2.09464 16 4.66797 16H11.3346C13.9073 16 16 13.9054 16 11.332V4.66536C16 2.0927 13.9054 0 11.332 0H4.66536ZM12.6667 2.66667C13.0347 2.66667 13.3333 2.96533 13.3333 3.33333C13.3333 3.70133 13.0347 4 12.6667 4C12.2987 4 12 3.70133 12 3.33333C12 2.96533 12.2987 2.66667 12.6667 2.66667ZM8 4C10.206 4 12 5.794 12 8C12 10.206 10.206 12 8 12C5.794 12 4 10.206 4 8C4 5.794 5.794 4 8 4ZM8 5.33333C7.29276 5.33333 6.61448 5.61428 6.11438 6.11438C5.61428 6.61448 5.33333 7.29276 5.33333 8C5.33333 8.70724 5.61428 9.38552 6.11438 9.88562C6.61448 10.3857 7.29276 10.6667 8 10.6667C8.70724 10.6667 9.38552 10.3857 9.88562 9.88562C10.3857 9.38552 10.6667 8.70724 10.6667 8C10.6667 7.29276 10.3857 6.61448 9.88562 6.11438C9.38552 5.61428 8.70724 5.33333 8 5.33333V5.33333Z" fill="currentColor"></path>
              </g>
            </svg>
          </a>
        </div>
      </div>
    );
  }
}

Footbar.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
};

export default Footbar
