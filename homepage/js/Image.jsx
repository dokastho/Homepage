import React from 'react';
import PropTypes from 'prop-types';

class Image extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const {
      id,
      keyNum
    } = this.props;
    return (
      <img src={`/api/v1/media/${id}/`} key={keyNum} className='image' />
    )
  }
}

Image.propTypes = {
  id: PropTypes.string.isRequired,
  keyNum: PropTypes.number.isRequired
};

export default Image
