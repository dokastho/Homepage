import PropTypes from 'prop-types';
import React from 'react'

class Headbar extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className='headbar'>
        <div className='headbar-item'><h5>Thomas Dokas</h5></div>
        <div className='headbar-item'><h5>@dokastho on all platforms</h5></div>
      </div>
    );
  }
}

Headbar.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
};

export default Headbar
