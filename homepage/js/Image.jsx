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
      <div>
        <img src={`/api/v1/media/${id}/`} key={keyNum} className='image' />
      </div>
    )
  }
}

Image.propTypes = {
  id: PropTypes.string.isRequired,
  keyNum: PropTypes.number.isRequired
};

export default Image
