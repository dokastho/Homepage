import PropTypes from 'prop-types';
import React from 'react'

class Thumbnail extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      pageId: props.pageId,
      title: props.title,
      description: props.description,
      pageSize: props.pageSize,
      thumbnailBlowUp: props.thumbnailBlowUp
    };
  }

  render() {
    const {
      pageId,
      title,
      description,
      pageSize,
      thumbnailBlowUp
    } = this.state;
    return (
      <div className={`item-card-${pageSize}`} key={pageId} onClick={() => {thumbnailBlowUp(pageId)}}>
        <div className="item-card-content">
          <h1>{title}</h1>
          <h4>{description}</h4>
        </div>
      </div>
    );
  }
}

Thumbnail.propTypes = {
  // prop types go here
  pageId: PropTypes.number.isRequired,
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  pageSize: PropTypes.number.isRequired,
  thumbnailBlowUp: PropTypes.func.isRequired
};

Thumbnail.defaultProps = {
  // default prop values go here if not required
};

export default Thumbnail
