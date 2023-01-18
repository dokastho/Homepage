import PropTypes from 'prop-types';
import { react } from 'react'

class Page extends react.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      pageId: props.pageId,
      title: props.title,
      description: props.description,
      body: props.body,
      route: props.route,
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
      body,
      route,
      pageSize
    } = this.state;
    return (
      <div className={`item-card-${pageSize}`} key={pageId}>
        <div className="item-card-content">
          <h1>{title}</h1>
          <h4>{description}</h4>
          <h4>{body}</h4>
          <h4>{route}</h4>
        </div>
      </div>
    );
  }
}

Page.propTypes = {
  // prop types go here
  pageId: PropTypes.number.isRequired,
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  body: PropTypes.string.isRequired,
  route: PropTypes.string.isRequired,
  pageSize: PropTypes.number.isRequired
};

Page.defaultProps = {
  // default prop values go here if not required
};

export default Page
