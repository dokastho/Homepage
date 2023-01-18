import PropTypes from 'prop-types';
import { react } from 'react'

class Thumbnail extends react.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      pageId: props.pageId,
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
      pageId,
      title,
      description,
      pageSize
    } = this.state;
    return (
      <div className={`item-card-${pageSize}`} key={pageId}>
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
  pageSize: PropTypes.number.isRequired
};

Thumbnail.defaultProps = {
  // default prop values go here if not required
};

export default Thumbnail
