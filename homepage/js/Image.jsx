import React from 'react';
import PropTypes from 'prop-types';

class Image extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const {
      id,
      keyNum,
      className
    } = this.props;
    const name = className || 'image'
    return (
      <img src={`/api/v1/media/${id}/`} key={keyNum} className={name} />
    )
  }
}

Image.propTypes = {
  id: PropTypes.string.isRequired,
  keyNum: PropTypes.number.isRequired,
  className: PropTypes.string,
};

export default Image
