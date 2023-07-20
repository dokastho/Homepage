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
      className,
      onLoad
    } = this.props;
    const name = className || 'image'
    return (
      <img src={`/api/v1/media/get/${id}/`} key={keyNum} className={name} onLoad={() => {onLoad()}} />
    )
  }
}

Image.propTypes = {
  id: PropTypes.string.isRequired,
  keyNum: PropTypes.number.isRequired,
  className: PropTypes.string,
  // onLoad
};

export default Image
