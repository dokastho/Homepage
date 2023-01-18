import PropTypes from 'prop-types';
import { react } from 'react'

class Page extends react.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      title: props.title,
      description: props.description,
      body: props.body,
      route: props.route,
    };
  }

  // componentDidMount() {
  //   this.setState(this.props);
  // }

  render() {
    const {
      title,
      description,
      body,
      route,
    } = this.state;
    return (
      <div className={"foobar"}>
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
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  body: PropTypes.string.isRequired,
  route: PropTypes.string.isRequired,
};

Page.defaultProps = {
  // default prop values go here if not required
};

export default Page
