import PropTypes from 'prop-types';
import React from 'react'

class Thumbnail extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      title: props.title,
      description: props.description,
      pageSize: props.pageSize
    };
  }

  // componentDidMount() {
  //   this.setState(this.props);
  // }

  render() {
    const {
      title,
      description,
      pageSize
    } = this.state;
    return (
      <div className={`item-card-${pageSize}`}>
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
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  pageSize: PropTypes.number.isRequired
};

Thumbnail.defaultProps = {
  // default prop values go here if not required
};

export default Thumbnail
