import PropTypes from 'prop-types';
import React from 'react'

class Headbar extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className='headbar'>
        <div className='headbar-item'>Thomas Dokas</div>
        <hr />
        <div className='headbar-item'>@dokastho on all platforms</div>
      </div>
    );
  }
}

Headbar.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
};

export default Headbar
